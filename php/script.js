var hbs = {
	change: function(target) {
		window.location.href = "subpage.php?p=" + target;
	}
};

$(document).ready(function() {
	var search = searchToObject();
	if(search.hasOwnProperty('p')) {
		$(".side-nav").find("a").each(function(i, e) {
			var id = e.id;
			var regex = /side-nav-(.+)/;
			var result = regex.exec(id);
			if(result != null) {
				if(search.p.indexOf(result[1]) == 0) {
					$(e).addClass("active");
				}
			}
		});
					
		(function() {
			var target = $("#cover img");
			var p =  search.p;
			var result = search.p.match(/(.+)\/?/)[1];
			console.log(result);
			if(target != null) {
				var s = "images/c_" + result + ".jpg";
				target.attr("src", s );
			}
		})();
	}

	function searchToObject() {
		var pairs = window.location.search.substring(1).split("&"),
			obj = {},
			pair,
			i;

		for (i in pairs) {
			if (pairs[i] === "") continue;

			pair = pairs[i].split("=");
			obj[decodeURIComponent(pair[0])] = decodeURIComponent(pair[1]);
		}
		return obj;
	}
});