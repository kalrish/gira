function gira_get_sequence
{
	declare \
		-r \
		branch="${1}" \
		#
	
	declare \
		-r \
		sequence_file_path="${HOME}/.cache/gira/${branch}" \
		#
	
	if exec 3< "${sequence_file_path}"
	then
		read sequence <&3
		
		echo "${sequence}"
		
		exec 2>&-
		
		declare \
			-i \
			return_code=0
	else
		declare \
			-i \
			return_code=1
	fi
	
	return ${return_code}
}
