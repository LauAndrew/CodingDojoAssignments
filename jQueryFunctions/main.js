$(document).ready(function(){
	$(".b1").click(function(){
		$(".b1").text("pizza");
	});

	$(".classT").hide(function(){
		$(".classT").hide();
	});

	$(document).on('click','#btn3',function(){
		$(".classM").show();
	});

	$(".toggleT").toggle(function(){
		$(".toggleT").toggle();
	});


	$(document).on('click','#btn2',function(){
		$(".toggleT").fadeOut();
	});

	// $(document).on('click','#btn2',function(){
	// 	$(".toggleT").toggle();
	// });

	$(document).on('click','#btn4',function(){
		$(".BP").addClass("new");
	});

	$(document).on('click','#btn4',function(){
		$(".BP").before("pepperoni");
	});

	$(document).on('click','#btn4',function(){
		$(".BP").after("cheese");
	});

	$(document).on('click','#btn4',function(){
		$(".pizza").append($("<h1>").text('FOOZ'));
	});

	$('#btn5').click(function(){
		$("#rob").html("<h1>Hola</h1>");
		
	});

	$("#btn5").click(function(){
		$('#fooz').attr('src','images/betterimage.jpg');

	});

    $(".btn6").click(function(){
        $("input:text").val("More Pizza please....");
    });
	






});