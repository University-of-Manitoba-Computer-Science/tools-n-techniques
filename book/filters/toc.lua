-- a collection of all tocs
tocs = {}

function Header(elem)
	if elem.level == 2 then
		return { elem, tocs[elem.identifier] }
	end
end

function Pandoc(doc)
	local chunks = pandoc.structure.split_into_chunks(doc, { chunk_level = 2 })
	-- each chunk is an h2 in the source document (chunk_level 2)
	for chunk_id, chunk in pairs(chunks.chunks) do
		-- make a toc for each h2 down to h4
		section_toc = pandoc.structure.table_of_contents(chunk.contents, { toc_depth = 4 })
		-- the toc is a list ([1] that contains the h2, so skip it [2])
		tocs[chunk.id] = section_toc.content[1][2]
	end
	-- Pandoc runs after Block, so re-run Header.
	return doc:walk({ Header = Header })
end
