window.addEventListener("load", setup);

// defining global variables
var bigMacElement;
var cheeseburgerElement;
var quarterPounderElement;
var frenchFriesElement;
var cocacolaElement;
var drPepperElement;
var fantaOrangeElement;
var spriteElement;
var cappuccinoElement;
var caramelMacchiatoElement;
var icedMochaElement;
var mochaLatteElement;
var bakedAppleElement;
var chocolateChipsCookieElement;
var hotFudgeSundaeElement;
var mcFlurryElement;
var orderSummaryElement;

function setup() {
    retrieveDOMReferences();
    addEventListeners();
}

function retrieveDOMReferences() {
    // burgers and co
    bigMacElement = document.getElementById("big_mac_id");
    cheeseburgerElement = document.getElementById("chesseburger_id");
    quarterPounderElement = document.getElementById("quarter_pounder_id");
    frenchFriesElement = document.getElementById("french_fries_id");

    // drinks
    cocacolaElement = document.getElementById("coca_cola_id");
    drPepperElement = document.getElementById("dr_pepper_id");
    fantaOrangeElement = document.getElementById("fanta_orange_id");
    spriteElement = document.getElementById("sprite_id");

    // coffees
    cappuccinoElement = document.getElementById("cappuccino_id");
    caramelMacchiatoElement = document.getElementById("caramel_macchiato_id");
    icedMochaElement = document.getElementById("iced_mocha_id");
    mochaLatteElement = document.getElementById("mocha_latte_id");

    // desserts
    bakedAppleElement = document.getElementById("baked_apple_id");
    chocolateChipsCookieElement = document.getElementById("chocolate_chips_cookie_id");
    hotFudgeSundaeElement = document.getElementById("hot_fudge_sundae_id");
    mcFlurryElement = document.getElementById("mc_flurry_id");

    // order summary text area
    orderSummaryElement = document.getElementById("order_summary");
}

function addEventListeners() {
    // burgers and Co.
    bigMacElement.addEventListener("keyup", updateOrderSummary);
    cheeseburgerElement.addEventListener("keyup", updateOrderSummary);
    quarterPounderElement.addEventListener("keyup", updateOrderSummary);
    frenchFriesElement.addEventListener("keyup", updateOrderSummary);

    // drinks
    cocacolaElement.addEventListener("keyup", updateOrderSummary);
    drPepperElement.addEventListener("keyup", updateOrderSummary);
    fantaOrangeElement.addEventListener("keyup", updateOrderSummary);
    spriteElement.addEventListener("keyup", updateOrderSummary);

    // coffees
    cappuccinoElement.addEventListener("keyup", updateOrderSummary);
    caramelMacchiatoElement.addEventListener("keyup", updateOrderSummary);
    icedMochaElement.addEventListener("keyup", updateOrderSummary);
    mochaLatteElement.addEventListener("keyup", updateOrderSummary);

    // desserts
    bakedAppleElement.addEventListener("keyup", updateOrderSummary);
    chocolateChipsCookieElement.addEventListener("keyup", updateOrderSummary);
    hotFudgeSundaeElement.addEventListener("keyup", updateOrderSummary);
    mcFlurryElement.addEventListener("clikeyupck", updateOrderSummary);
}

function updateOrderSummary() {

    const formatter = new Intl.NumberFormat('en-US', {
        style: 'currency',
        currency: 'USD',
    });

    orderSummaryElement.value = "";

    // burgers order
    if(bigMacElement.value != 0) {
        orderSummaryElement.value += `${bigMacElement.value} Big Mac(s)  ${formatter.format(parseInt(bigMacElement.value)* 2.00)}\n`;
    }

    if (cheeseburgerElement.value !=0 ) { 
        orderSummaryElement.value += `${cheeseburgerElement.value} Cheeseburger(s)  ${formatter.format(parseInt(cheeseburgerElement.value)* 1.50)}\n`;
    }

    if (quarterPounderElement.value != 0) {
        orderSummaryElement.value += `${quarterPounderElement.value} Quarter Pounder(s)  ${formatter.format(parseInt(quarterPounderElement.value)* 2.50)}\n`;
    }

    if (frenchFriesElement.value != 0) {
        orderSummaryElement.value += `${frenchFriesElement.value} French Fries(s)  ${formatter.format(parseInt(frenchFriesElement.value)* 2.50)}\n`;
    }

    // drinks
    if (cocacolaElement.value !=0 ) {
        orderSummaryElement.value += `${cocacolaElement.value} Coca-cola(s)  ${formatter.format(parseInt(cocacolaElement.value)* 2.50)}\n`;
    }

    if (drPepperElement.value !=0 ) {
        orderSummaryElement.value += `${drPepperElement.value} Dr. Pepper(s)  ${formatter.format(parseInt(drPepperElement.value)* 2.50)}\n`;
    }
    
    if (fantaOrangeElement.value !=0 ) {
        orderSummaryElement.value += `${fantaOrangeElement.value} Fanta Orange(s)  ${formatter.format(parseInt(fantaOrangeElement.value)* 2.50)}\n`;
    }
    
    if (spriteElement.value !=0 ) {
        orderSummaryElement.value += `${spriteElement.value} Sprite(s)  ${formatter.format(parseInt(spriteElement.value)* 2.50)}\n`;
    }

    // coffees
    if (cappuccinoElement.value !=0 ) {
        orderSummaryElement.value += `${cappuccinoElement.value} Cappuccino(s)  ${formatter.format(parseInt(cappuccinoElement.value)* 2.50)}\n`;
    }
        
    if (caramelMacchiatoElement.value !=0 ) {
        orderSummaryElement.value += `${caramelMacchiatoElement.value} Caramel Macchiato(s)  ${formatter.format(parseInt(caramelMacchiatoElement.value)* 2.50)}\n`;
    }

    if (icedMochaElement.value !=0 ) {
        orderSummaryElement.value += `${icedMochaElement.value} Iced Mocha(s)  ${formatter.format(parseInt(icedMochaElement.value)* 2.50)}\n`;
    }
        
    if (mochaLatteElement.value !=0 ) {
        orderSummaryElement.value += `${mochaLatteElement.value} Mocha Latte(s)  ${formatter.format(parseInt(mochaLatteElement.value)* 2.50)}\n`;
    }

    // desserts
    if (bakedAppleElement.value !=0 ) {
        orderSummaryElement.value += `${bakedAppleElement.value} Baked Apple(s)  ${formatter.format(parseInt(bakedAppleElement.value)* 2.50)}\n`;
    }

    if (chocolateChipsCookieElement.value !=0 ) {
        orderSummaryElement.value += `${chocolateChipsCookieElement.value} Chocolate Chips Cookie(s)  ${formatter.format(parseInt(chocolateChipsCookieElement.value)* 2.50)}\n`;
    }

    if (hotFudgeSundaeElement.value !=0 ) {
        orderSummaryElement.value += `${hotFudgeSundaeElement.value} Hot Fudge Sundae(s)  ${formatter.format(parseInt(hotFudgeSundaeElement.value)* 2.50)}\n`;
    }

    if (mcFlurryElement.value !=0 ) {
        orderSummaryElement.value += `${mcFlurryElement.value} Mac Flurry(s)  ${formatter.format(parseInt(mcFlurryElement.value)* 2.50)}\n`;
    }
}

