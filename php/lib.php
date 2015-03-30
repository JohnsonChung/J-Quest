<?php
function tpl($target) {
	echo file_get_contents("js/templates/$target.hbs");
}

function main() {
	if (isset($_GET['p'])) {
		$pages = array(
			'concept',
			'service',
			'howto',
			'shop',
			'campaign',
			'recruit',
			'faq',
			'about',
			'contact',
		);

		if (in_array($_GET['p'], $pages)) {
			echo file_get_contents('js/templates/' . $_GET['p'] . '.hbs');
		}
	}
}