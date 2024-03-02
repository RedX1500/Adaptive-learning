<?php


require('../../config.php');
require_once($CFG->libdir . '/adminlib.php');

$path = optional_param('path', '', PARAM_PATH); // $nameofarray = optional_param_array('nameofarray', null, PARAM_INT);
$pageparams = array();

if ($path) {
	$pageparams['path'] = $path;
}

global $CFG, $USER, $DB, $OUTPUT, $PAGE;

$PAGE->set_url('/local/slack/userdata.php');

require_login();

$PAGE->set_pagelayout('admin');
$context = context_system::instance();
$PAGE->set_context($context);

admin_externalpage_setup('userdata', '', $pageparams);

$header = $SITE->fullname;
$PAGE->set_title(get_string('pluginname', 'local_slack'));
$PAGE->set_heading($header);

echo $OUTPUT->header();

/* Add your custom code here..*/

echo $OUTPUT->footer();
