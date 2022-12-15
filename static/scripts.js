/*


//addapted from w3schools and colleague Cole Pearson
function qrScanner(){
  function onScanSuccess(decodedText, decodedResult){ //adapted from https://blog.minhazav.dev/research/html5-qrcode
    console.log("Scan result: ${decodedText}", decodedResult);
    window.open(decodedText);  //opens a new tab with the URL
  }
  var qrScanner = new Html5QrcodeScanner(
    "reader", { fps: 10, qrbox: 250 }); //inserts the scanner in div in scanner.html with the id "reader"
  qrScanner.render(onScanSuccess);
}
