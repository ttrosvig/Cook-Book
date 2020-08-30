$("#get-recipe").on("click", async function () {
    resp = await axios.get('https://api.spoonacular.com/recipes/random?tags=dessert&number=1&apiKey=76d7a5ae655a48daab0f3fcbd50a5a28');

    title = resp.data.recipes[0].title;

    url = resp.data.recipes[0].sourceUrl;

    $info = $("#information-area");

    $info.empty();
    $('#link-area').empty()

    $info.append(title);
    
    $link = $("<a>View Recipe</a>");
    $("#link-area").append($link);

    $link.attr("href", url)
})