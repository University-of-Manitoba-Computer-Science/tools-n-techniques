function Math(elem)
	if elem.text:match("\\LaTeX") then
		return pandoc.RawInline("typst", "#LaTeX")
	end
end
