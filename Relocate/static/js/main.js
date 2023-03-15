$(function(){
    // Material Select Initialization
    $(document).ready(function() {
        $('.mdb-select').material_select();
       
    });

    $('.btn-icon-dropdown-toggle').dropdown();

    // Initialize Quill editor 
    if($('#editor').length >= 1) {
        var editor = new Quill('#editor', {
            modules: {
                toolbar: [
                    [{ header: [1, 2, false] }],
                    ['bold', 'italic', 'underline'],
                    ['image', 'code-block']
                ]
            },
            placeholder: 'Compose an epic...',
            theme: 'snow'  // or 'bubble'
        });
    }
});