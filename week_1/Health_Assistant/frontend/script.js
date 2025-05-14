document.getElementById("fitness-form").addEventListener("submit", async function(event) {
    event.preventDefault();
    const height = document.getElementById("height").value;
    const weight = document.getElementById("weight").value;
    const activity = document.getElementById("activity").value;

    const response = await fetch("http://localhost:8000/api/fitness",{
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            height: height,
            weight: weight,
            activity: activity
        })
    })
    const data = await response.json();
    document.getElementById("results").innerHTML = `
    <h3>AI Recommendations:</h3>
    ${data.message}
    `;

});

