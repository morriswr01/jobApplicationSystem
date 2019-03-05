$(document).ready(function () {

    // Remove empty fields from GET forms
    $("form").submit(function () {
        $(this).find(":input").filter(function () {
            return !this.value;
        }).attr("disabled", "disabled");
        return true; // ensure form still submits
    });
    // Un-disable form fields when page loads, in case they click back after submission
    $("form").find(":input").prop("disabled", false);


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

    //Show show account settings modal
    $('#account-settings-button').click(function () {
        target = $('#account-settings-modal');

        target.css("display", "block");
    });

    $('#new-job-button').click(function () {
        target = $('#add-new-job-modal');

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
        $('.application').not(target).hide();

        $(target).toggle('fast');
    });

    // CREATEAPPLICATION PAGE

    //Populate languages dropdown
    var languages = ["SQL", "Javascript", "Java", "C#", "Python", "C++", "PHP", "Ruby", "Swift"];
    var options = '';
    languages.forEach(language => {
        options += '<option value="' + language + '">' + language + '</option>';
    });
    $('#progLangName').append(options);

    //Populate Number of years of employment worked
    options = '';
    for (let i = 0; i < 50; i++) {
        options += '<option value="' + i + '">' + i + ' years</option>';
    }
    options += '<option value="50">50+</option>';
    $('#years').append(options);

    //Add new a-level on clicking add
    $('.add-input').click(function (e) {
        e.preventDefault();
        appendDiv = $(this).parent().siblings().first().next();
        fieldName = appendDiv.attr('id');
        nameInput = $(this).siblings().first();
        gradeOrProficiency = $(this).siblings().first().next();

        if (nameInput.val() != "" && gradeOrProficiency.val() != "") {
            $(appendDiv).append('<div class="threeColumnFields"><input type="text" name="' + fieldName + '[name]" value="' + nameInput.val() + '" readonly="readonly" /><input type="text" name="' + fieldName + '[proficiency]" value="' + gradeOrProficiency.val() + '" readonly="readonly" /><i class="remove material-icons">close</i></div>');
            $('.resetSelect').prop('selectedIndex', 0);
            nameInput.val("");
            gradeOrProficiency.val("");
        }
    });

    //Add employment on clicking add
    $('.add-prev-employment').click(function (e) {
        e.preventDefault();
        nameInput = $('#companyName');
        postName = $('#postName');
        lengthYears = $('#years');
        lengthMonths = $('#months');

        if (nameInput.val() != "" && postName.val() != "" && lengthYears.val() != "" && lengthMonths.val() != "") {
            console.log('these are not empty');
            $('.prevEmploymentDetails').append('<div class="company"><input type="text" name="previousEmployment[companyName]" readonly="readonly" value="' + nameInput.val() + '" /><input type="text" name="previousEmployment[postName]" readonly="readonly" value="' + postName.val() + '" /> <div class="threeColumnFields employmentLength"> <input type="text" name="previousEmployment[lengthYears]" readonly="readonly" value="' + lengthYears.val() + '" /><input type="text" name="previousEmployment[lengthMonths]" readonly="readonly" value="' + lengthMonths.val() + '" /><i class="remove-employment material-icons">close</i></div>');

            $('.resetSelect').prop('selectedIndex', 0);
            nameInput.val("");
            postName.val("");
        }
    });

    //A Remove input
    $('body').on('click', '.remove', function (e) {
        $(this).parent().remove();
    });

    //A Remove employment
    $('body').on('click', '.remove-employment', function (e) {
        $(this).parent().parent().remove();
    });


});