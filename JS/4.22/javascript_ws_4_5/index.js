const player1 = document.querySelector('#player1-img')
const player2 = document.querySelector('#player2-img')
const countA = document.querySelector('.countA')
const countB = document.querySelector('.countB')
const scissorsButton = document.querySelector("#scissors-button")
const rockButton = document.querySelector("#rock-button")
const paperButton = document.querySelector("#paper-button")
const modalTag = document.querySelector(".modal")
const modalTextTag = document.querySelector(".modal-content")
let count1 = 0
let count2 = 0

const playGame = function(player1Choice, player2Choice) {
    let result = 0;
  
    if (player1Choice === player2Choice) {
      result = 0;
    } else if (
      (player1Choice === "scissors" && player2Choice === "rock") ||
      (player1Choice === "rock" && player2Choice === "paper") ||
      (player1Choice === "paper" && player2Choice === "scissors")
    ) {
      result = 2;
      count2++;
      countB.textContent = count2
    } else {
      result = 1;
      count1++;
      countA.textContent = count1
    }
  
    return result
}

const buttonClickHandler = function(choice) {
    console.log(choice)
    player1.setAttribute('src', `./img/${choice}.png`)
    scissorsButton.disabled = true;
    rockButton.disabled = true;
    paperButton.disabled = true;
    
    let setIntervalID
    const choice_list = ['rock', 'scissors', 'paper']
    const img_change = function () {
        const randomChoice = choice_list[Math.floor(Math.random()*choice_list.length)]
        player2.setAttribute('src', `./img/${randomChoice}.png`)
    }
    setIntervalID = setInterval(img_change, 100)
    const stopintervalID = function() {
        clearInterval(setIntervalID)
    }
    setInterval(stopintervalID, 2900)
    
    setTimeout(() => {
        const player2Choice = choice_list[Math.floor(Math.random()*choice_list.length)]
        player2.setAttribute('src', `./img/${player2Choice}.png`)
        const result = playGame(choice, player2Choice);
        console.log(result)
        console.log(player2Choice)
        
        if (result === 0) {
            modalTag.style.display = 'block'
            modalTextTag.textContent = "It's a tie!"
        } else if (result === 1) {
            modalTag.style.display = 'block'
            modalTextTag.textContent = "Player 1 wins!"
        } else if (result === 2) {
            modalTag.style.display = 'block'
            modalTextTag.textContent = "Player 2 wins!"
        }
        
        scissorsButton.disabled = false;
        rockButton.disabled = false;
        paperButton.disabled = false;
    }, 3000);
    
    setTimeout(() => {modalTag.style.display = 'none', player1.setAttribute('src', "./img/scissors.png")
    }, 5000)
    }   

  scissorsButton.addEventListener('click', () => buttonClickHandler("scissors"))
  rockButton.addEventListener('click', () => buttonClickHandler('rock'))
  paperButton.addEventListener('click', () => buttonClickHandler('paper'))