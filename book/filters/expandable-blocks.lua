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
				pandoc.RawBlock("typst", string.format("#block[#emph[%s] #emoji.arrow.b.curve", title)),
				pandoc.RawBlock("typst", "#block(inset: (left: 10%))["),
				elem,
				pandoc.RawBlock("typst", "]]"),
			}
		end
	end
end
