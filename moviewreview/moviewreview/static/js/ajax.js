$(function(){

var inp=$("#search");
//if(inp.val().length>0)

  $('.btnSearch').click(function() {

   $.ajax({
         type: "POST",
         url: "/movies/search/",
	 data:{
		'search_text' : $('#search').val(),
		'csrfmiddlewaretoken' : $("input[name=csrfmiddlewaretoken]").val()
	      },
		success: searchSuccess,
		dataType: 'html'
	  });
	});
});

function searchSuccess(data, textStatus,jqXHR)
{
  $('#search-results').html(data);
}