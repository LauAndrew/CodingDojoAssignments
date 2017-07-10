$(document).ready(function(){
	
	$('button').click(function(){
		var info = []
		$('form#addusers :input').each(function(){
			info.push($(this).val());
		});
			$("tbody").append("<tr><td>"+info[0]+"</td><td>"+info[1]+"</td><td>"+info[2]+"</td><td>"+info[3]+"</td></tr>");
		});
		info =[];
	})

	


	
// 	$ ("input") .change (displayVals);
// 	displayVals();