if exists("loaded_my_plugin")
	finish
endif
let loaded_my_plugin = 1

"Combine lines into one line, each line with pattern replacement
function s:ReplacePerLine(pat, arg)
	let curtxt = substitute(a:pat, a:arg, getline('.'), "g")
	call setline('.', curtxt)
endfunction

"绑定快捷键 - 方法一
noremap <leader>r :%call <SID>ReplacePerLine("#","#")
