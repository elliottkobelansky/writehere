let textArea = document.getEleentById("textbox");
let characterCounter = document.getElementById("char_count");
const maxNumOfChars = 200;

const countCharacters = () => {
    let numOfEnteredChars = textArea.value.length;
    let counter = maxNumOfChars - numOfEnteredChars;
    characterCounter.textContent = counter + "/100";
};

textArea.addEventListener("input", countCharacters);

