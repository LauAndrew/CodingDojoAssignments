$(document).ready(function(){



			

			for (var i = 1; i < 152; i++){
				
					$("#pokemonS").append('<img id=\''+i+'\' src="http://pokeapi.co/media/img/' + i + '.png">');
				}




			$("img").click(function(){

				$("#pokeimg").attr('src','http://pokeapi.co/media/img/' + $(this).attr('id') + '.png');



				$.get("http://pokeapi.co/api/v1/pokemon/"+$(this).attr("id"), function( data ) {
					  $("#pokename").html( data.name );
					  $("#pokeheight").html( data.height );
					  $("#pokeweight").html( data.weight );
					  $("#pokename").html( data.name );
					  $("#poketype").html("<ul>");

					  for(var i=0;i<data.types.length;i++){
					  	$("#poketype").append('<li>'+data.types[i].name+'</li>');

					  }
						$("#poketype").append("</ul>");


						// document.getElementById('pokename').innerHTML=data.name;

				});


			})	
				


	})