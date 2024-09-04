local ffi = require("ffi")

ffi.cdef[[
    int __stdcall OpenClipboard(void* hwnd);
    int __stdcall EmptyClipboard();
    void* __stdcall GlobalAlloc(int flags, int size);
    void* __stdcall GlobalLock(void* handle);
    int __stdcall GlobalUnlock(void* handle);
    void* __stdcall memcpy(void* dest, const void* src, size_t count);
    int __stdcall SetClipboardData(unsigned int uFormat, void* hMem);
    int __stdcall CloseClipboard();
    int __stdcall GlobalFree(void* handle);
    int __stdcall MultiByteToWideChar(unsigned int CodePage, unsigned int dwFlags,
                                      const char* lpMultiByteStr, int cbMultiByte,
                                      wchar_t* lpWideCharStr, int cchWideChar);
]]

local CF_UNICODETEXT = 13
local GMEM_MOVEABLE = 0x0002

-- Helper function to convert a UTF-8 string to UTF-16
local function utf8_to_utf16(utf8_str)
    local wchar_t = ffi.typeof("wchar_t[?]")
    local wsize = ffi.C.MultiByteToWideChar(65001, 0, utf8_str, #utf8_str, nil, 0)
    local wstr = ffi.new(wchar_t, wsize + 1) -- +1 for the null terminator
    ffi.C.MultiByteToWideChar(65001, 0, utf8_str, #utf8_str, wstr, wsize)
    return wstr, (wsize + 1) * 2 -- Return the UTF-16 string and its byte size
end

function copy_to_clipboard(text)
    local wstr, size = utf8_to_utf16(text)
    if ffi.C.OpenClipboard(nil) ~= 0 then
        ffi.C.EmptyClipboard()
        local hMem = ffi.C.GlobalAlloc(GMEM_MOVEABLE, size)
        local ptr = ffi.C.GlobalLock(hMem)
        ffi.C.memcpy(ptr, wstr, size)
        ffi.C.GlobalUnlock(hMem)
        ffi.C.SetClipboardData(CF_UNICODETEXT, hMem)
        ffi.C.CloseClipboard()
        -- Note: Do not call GlobalFree(hMem) here, as the clipboard now owns the memory
    end
end

function copy_subtitle()
    local subtitle = mp.get_property("sub-text")
    if subtitle and subtitle ~= "" then
        local identifier = "[MPV]"
        local modified_subtitle = identifier .. subtitle
        local platform = detect_platform()
        if platform == "windows" then
            copy_to_clipboard(modified_subtitle)
        elseif platform == "macos" then
            os.execute(string.format("echo '%s' | pbcopy", modified_subtitle:gsub("'", "'\\''")))
        elseif platform == "linux" then
            os.execute(string.format("echo '%s' | xclip -selection clipboard", modified_subtitle:gsub("'", "'\\''")))
        end
        -- mp.osd_message("Subtitle copied to clipboard")
    end
end

function detect_platform()
    local o = {}
    if mp.get_property_native('options/vo-mmcss-profile', o) ~= o then
        return 'windows'
    elseif mp.get_property_native('options/cocoa-force-dedicated-gpu', o) ~= o then
        return 'macos'
    end
    return 'linux'
end

-- Register an observer for the 'sub-text' property
mp.observe_property("sub-text", "string", copy_subtitle)
