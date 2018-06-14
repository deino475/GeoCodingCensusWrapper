<?php
class Geocoding {

	public function request($data) {
		$base_url = "https://geocoding.geo.census.gov/geocoder/geographies/address?benchmark=Public_AR_Census2010&format=json&vintage=Census2010_Census2010&layers=14&";
		$extension = http_build_query($data);
		$url = $base_url . $extension;
		$ch = curl_init($url);
		curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
		$resp = curl_exec($ch);
		curl_close($ch);
		return json_decode($resp, true);
	}
}

$x =  new Geocoding();
$resp = $x->request(['street' => '5619 Belarbor Street', 'city' => 'Houston', 'state' => 'TX', 'zip' => '77033']);
?>
