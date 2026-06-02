function Div(elem)
	if elem.classes:find("expandable") then
		local title = elem.attributes["title"]
		if FORMAT:match("html") then
			return {
				pandoc.RawBlock("html", string.format("<details><summary>%s</summary>", title)),
				elem,
				pandoc.RawBlock("html", "</details>"),
			}
		elseif FORMAT:match("typst") then
			return {
				pandoc.RawBlock("typst", string.format("#strong[#smallcaps[%s]]", title)),
				elem,
			}
		end
	end
end
