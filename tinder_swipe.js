function loop() {
    var rand = Math.round(Math.random() * 5000) + 1000;
    setTimeout(function() {
            var element = document.querySelector('[aria-label="Like"]');
			element.click()
            loop();  
    }, rand);
}
loop();
