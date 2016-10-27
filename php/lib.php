<?php
function tpl($target) {
	echo file_get_contents("templates/$target");
}

function main() {
	global $env;

	$env = strstr($_SERVER['HTTP_HOST'], 'j-quest.jp') ? 'production' : 'testing';

	if (isset($_GET['p'])) {
		$pages = array(
			"sideNav",
			"about",
			"campaign",
			"concept",
            "contact",
            "contact2",
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
			"contactKeeperCampaign",
			"shopKeeperCampaign",
		);

		if (in_array($_GET['p'], $pages)) {

			switch ($_GET['p']) {
				case "recruit":
					$p = "recruit/recruit-index";
                    break;
				default:
					$p = $_GET['p'];
			}

			include 'templates/' . $p . '.hbs';
		}
	}
}

function isProduction() {
	global $env;
	return $env === 'production';
}