const characters = [
    document.getElementById('character1'),
    document.getElementById('character2'),
    document.getElementById('character3'),
    document.getElementById('character4'),
    document.getElementById('character5'),
    document.getElementById('character6'),
    document.getElementById('character7'),
    document.getElementById('character8'),
    document.getElementById('character9'),
    document.getElementById('character10'),
    document.getElementById('qrcode')
  ];
  
  function animateCharacter(character) {
    const x = Math.random() * (window.innerWidth - character.clientWidth * 2) + character.clientWidth / 2;
    const y = Math.random() * (window.innerHeight - character.clientHeight * 2) + character.clientHeight / 2;
    const duration = Math.random() * 3000 + 3000;
  
    character.animate([
      { transform: `translate(${x}px, ${y}px)` },
    ], {
      duration: duration,
      easing: 'linear',
      fill: 'forwards',
    });
  
    setTimeout(() => {
      animateCharacter(character);
    }, duration);
  }
  
  characters.forEach(character => {
    animateCharacter(character);
  
    // Add an event listener for the 'click' event to apply the spinning animation
    character.addEventListener('click', () => {
      character.animate([
        { transform: 'rotate(0deg)' },
        { transform: 'rotate(360deg)' },
      ], {
        duration: 500,
        iterations: 1,
        easing: 'linear',
      });
    });
  });
  