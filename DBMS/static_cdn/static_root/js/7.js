	$(document).ready(function() {
		$('#nav').onePageNav({
			begin: function() {
			console.log('start')
			},
			end: function() {
			console.log('stop')
			}
		});
	});