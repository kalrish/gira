function gira_get_sequence
{
	declare \
		-r \
		branch="${1}" \
		#
	
	declare \
		-r \
		cache_home="${XDG_CACHE_HOME:-${HOME}/.cache}" \
		#
	
	declare \
		-r \
		sequence_file_path="${cache_home}/gira/${branch}" \
		#
	
	if [[ -r "${sequence_file_path}" ]]
	then
		read \
			sequence \
			< "${sequence_file_path}" \
			#
		
		echo "${sequence}"
		
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
