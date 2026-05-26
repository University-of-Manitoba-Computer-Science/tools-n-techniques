function Div(elem)
	if elem.classes:find("outcomes") then
		return {
			pandoc.RawBlock("typst", '#rect(width: 100%, stroke: (dash: "dashed"))[#emoji.checkmark.box'),
			pandoc.Strong({ pandoc.Str("Learning outcomes") }),
			elem,
			pandoc.RawBlock("typst", "]"),
		}
	end

	if elem.classes:find("input") then
		return {
			pandoc.RawBlock("typst", "#emoji.keyboard"),
			pandoc.Strong({ pandoc.Str("Input") }),
			elem,
		}
	end

	if elem.classes:find("output") then
		return {
			pandoc.RawBlock("typst", "#emoji.printer"),
			pandoc.Strong({ pandoc.Str("Output") }),
			elem,
		}
	end

	if elem.classes:find("example") then
		return {
			pandoc.RawBlock("typst", '#rect(width: 100%, stroke: (dash: "dashed"))[#emoji.rocket'),
			pandoc.Strong({ pandoc.Str("Example") }),
			elem,
			pandoc.RawBlock("typst", "]"),
		}
	end
end
