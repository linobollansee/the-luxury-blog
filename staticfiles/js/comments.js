// Get all elements with the class name "btn-edit" which represent edit buttons for comments
const editButtons = document.getElementsByClassName("btn-edit");

// Get the input element where the comment text will be entered or edited
const commentText = document.getElementById("id_body");

// Get the form element for submitting comments
const commentForm = document.getElementById("commentForm");

// Get the submit button element for submitting the form
const submitButton = document.getElementById("submitButton");

// Initialize a Bootstrap modal for confirming deletion of comments
const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));

// Get all elements with the class name "btn-delete" which represent delete buttons for comments
const deleteButtons = document.getElementsByClassName("btn-delete");

// Get the element that confirms the deletion action
const deleteConfirm = document.getElementById("deleteConfirm");

// Loop through each edit button to add an event listener for the click event
for (let button of editButtons) {
    // When the edit button is clicked, this function is executed
    button.addEventListener("click", (e) => {
        // Get the comment ID from the data attribute of the clicked button
        let commentId = e.target.getAttribute("data-comment_id");

        // Retrieve the current content of the comment using its ID
        let commentContent = document.getElementById(`comment${commentId}`).innerText;
        
        // Set the value of the comment text input to the current comment content
        commentText.value = commentContent;

        // Change the text of the submit button to indicate the action will be an update
        submitButton.innerText = "Update";

        // Update the action attribute of the form to point to the edit comment endpoint with the comment ID
        commentForm.setAttribute("action", `edit_comment/${commentId}`);
        
        // Add a class to the comment text input to apply a highlighting animation
        commentText.classList.add("edit-highlight");
        
        // Remove the highlight class after 1 second to reset the style
        setTimeout(() => {
            commentText.classList.remove("edit-highlight");
        }, 1000); // Time set to 1000 milliseconds (1 second)
    });
}

// Loop through each delete button to add an event listener for the click event
for (let button of deleteButtons) {
    // When the delete button is clicked, this function is executed
    button.addEventListener("click", (e) => {
        // Get the comment ID from the data attribute of the clicked button
        let commentId = e.target.getAttribute("data-comment_id");

        // Set the href attribute of the delete confirmation link to the delete comment endpoint with the comment ID
        deleteConfirm.href = `delete_comment/${commentId}`;
        
        // Show the delete confirmation modal
        deleteModal.show();
        
        // Get the modal element to apply animations
        const modalElement = document.getElementById("deleteModal");

        // Add a shake animation class to the modal for visual effect
        modalElement.classList.add("modal-shake");

        // Remove the shake animation class after 0.5 seconds to reset the animation
        setTimeout(() => {
            modalElement.classList.remove("modal-shake");
        }, 500); // Time set to 500 milliseconds (0.5 seconds)
    });
}
