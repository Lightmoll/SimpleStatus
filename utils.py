def html_sanatize(in_str):
	in_str = in_str.replace("&", "&amp;")
	in_str = in_str.replace("<", "&lt;")
	in_str = in_str.replace(">", "&gt;")
	in_str = in_str.replace("\"", "&quot;")
	in_str = in_str.replace("'", "&apos;")
	in_str = in_str.replace("\r\n", "<br>")
	in_str = in_str.replace("\r", "<br>")
	in_str = in_str.replace("\n", "<br>")

	return in_str
