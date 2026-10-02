function Div(elem)
	if elem.classes:find("expandable") then
		local title = elem.attributes["title"]
        local group = elem.attributes["group"]
		if FORMAT:match("html") then
			return {
				pandoc.RawBlock("html", string.format("<details name='%s'><summary>%s</summary>", group, title)),
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
