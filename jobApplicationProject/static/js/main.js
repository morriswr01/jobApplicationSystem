$(document).ready(function () {
    //Show applicant login modal
    $('#applicant-login-button').click(function () {
        target = $('#applicant-login-modal');

        target.css("display", "block");
    });

    //Show admin login modal
    $('#admin-login-button').click(function () {
        target = $('#admin-login-modal');

        target.css("display", "block");
    });

    //Show admin login modal
    $('#account-settings-button').click(function () {
        target = $('#account-settings-modal');

        target.css("display", "block");
    });

    //Close modals on clicking cross button
    $('.close-modal').click(function () {
        target = $(this).parent().parent().parent();

        target.css("display", "none");
    });

    //Show accordion upon selecting a job to view
    $('.selectJob').on('click', function (e) {
        target = $(this).next().first();

        $('.jobDesc').not(target).hide();

        $(target).toggle('fast');
    });
});