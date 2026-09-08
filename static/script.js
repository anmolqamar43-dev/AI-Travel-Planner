// ==========================================
// Elements
// ==========================================

const form = document.getElementById("travelForm");

const generateBtn =
    document.getElementById("generateBtn");

const loading =
    document.getElementById("loading");

const errorBox =
    document.getElementById("error");

const result =
    document.getElementById("result");

const itinerary =
    document.getElementById("itinerary");

const techniqueInput =
    document.getElementById("technique");

const resultTechnique =
    document.getElementById("resultTechnique");


// ==========================================
// Technique buttons
// ==========================================

const techniqueButtons =
    document.querySelectorAll(".technique-btn");


techniqueButtons.forEach(button => {

    button.addEventListener("click", () => {

        // Remove active class
        techniqueButtons.forEach(btn => {
            btn.classList.remove("active");
        });

        // Add active class
        button.classList.add("active");

        // Store selected technique
        techniqueInput.value =
            button.dataset.technique;

    });

});


// ==========================================
// Form submission
// ==========================================

form.addEventListener("submit", async (event) => {

    event.preventDefault();


    // Hide old messages
    errorBox.classList.add("hidden");

    result.classList.add("hidden");


    // Get interests
    const selectedInterests =
        Array.from(
            document.querySelectorAll(
                'input[name="interests"]:checked'
            )
        ).map(
            checkbox => checkbox.value
        );


    // Validate interests
    if (selectedInterests.length === 0) {

        showError(
            "Please select at least one interest."
        );

        return;
    }


    // Collect form data
    const travelData = {

        name:
            document.getElementById("name").value.trim(),

        destination:
            document
                .getElementById("destination")
                .value
                .trim(),

        days:
            Number(
                document.getElementById("days").value
            ),

        budget:
            Number(
                document.getElementById("budget").value
            ),

        interests:
            selectedInterests,

        travel_style:
            document.getElementById("travelStyle").value,

        technique:
            techniqueInput.value
    };


    // Start loading
    setLoading(true);


    try {

        const response = await fetch(
            "/generate",
            {
                method: "POST",

                headers: {
                    "Content-Type":
                        "application/json"
                },

                body:
                    JSON.stringify(travelData)
            }
        );


        const data =
            await response.json();


        if (!response.ok || !data.success) {

            throw new Error(
                data.error ||
                "Something went wrong."
            );

        }


        // Display itinerary
        itinerary.textContent =
            data.itinerary;


        // Display technique
        resultTechnique.textContent =
            formatTechnique(
                data.technique
            );


        // Show result
        result.classList.remove(
            "hidden"
        );


        // Scroll to result
        result.scrollIntoView({
            behavior: "smooth"
        });

    }

    catch (error) {

        console.error(error);

        showError(
            error.message ||
            "Unable to generate travel plan."
        );

    }

    finally {

        setLoading(false);

    }

});


// ==========================================
// Loading state
// ==========================================

function setLoading(isLoading) {

    if (isLoading) {

        loading.classList.remove(
            "hidden"
        );

        generateBtn.disabled = true;

        generateBtn.textContent =
            "⏳ Generating...";

    }

    else {

        loading.classList.add(
            "hidden"
        );

        generateBtn.disabled = false;

        generateBtn.textContent =
            "✨ Generate Travel Plan";

    }

}


// ==========================================
// Error
// ==========================================

function showError(message) {

    errorBox.textContent =
        message;

    errorBox.classList.remove(
        "hidden"
    );

    errorBox.scrollIntoView({
        behavior: "smooth"
    });

}


// ==========================================
// Technique name
// ==========================================

function formatTechnique(technique) {

    if (technique === "zero-shot") {
        return "Zero-Shot";
    }

    if (technique === "few-shot") {
        return "Few-Shot";
    }

    if (technique === "structured") {
        return "Structured Reasoning";
    }

    return technique;
}