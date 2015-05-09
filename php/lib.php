<?php
function tpl($target) {
	echo file_get_contents("templates/$target");
}

function main() {
	if (isset($_GET['p'])) {
		$pages = array(
			"sideNav",
			"about",
			"campaign",
			"concept",
			"contact",
			"faq",
			"howto",
			"privacy",
			"recruit",
			"recruit/recruit-index",
			"recruit/recruit-form",
			"recruit/recruit-manager",
			"recruit/recruit-merit",
			"recruit/recruit-oshiete",
			"recruit/recruit-parttimer",
			"recruit/recruit-pts",
			"recruit/recruit-voice",
			"recruit/recruit-work",
			"service",
			"shop",
		);

		if (in_array($_GET['p'], $pages)) {

			switch ($_GET['p']) {
				case "recruit":
					$p = "recruit/recruit-index";
                    break;
				default:
					$p = $_GET['p'];
			}

			echo file_get_contents('templates/' . $p . '.hbs');
		}
	}
}
