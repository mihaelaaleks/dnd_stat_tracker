const int PIN_BTN_1 = 4;
const int PIN_BTN_2 = 7;

const int DEBOUNCE_DELAY_BTN_1 = 50;
const int DEBOUNCE_DELAY_BTN_2 = 50;

//variables that will change
int lastSteadyStateBtn1 = LOW;
int lastReadableStateBtn1 = LOW;
int currentStateBtn1;

int lastSteadyStateBtn2 = LOW;
int lastReadableStateBtn2 = LOW;
int currentStateBtn2;

unsigned long lastDebounceTimeBtn1 = 0;
unsigned long lastDebounceTimeBtn2 = 0;

int diceNumber = 0;

String diceArray[7] = {"D100", "D20", "D12", "D10", "D8", "D6", "D4"};

void setup() {
  Serial.begin(9600);
  //pull-up input pin will be high when the switch is open
  //and low when it is closed
  pinMode(PIN_BTN_1, INPUT_PULLUP);
  pinMode(PIN_BTN_2, INPUT_PULLUP);
}

void loop() {

  currentStateBtn1 = digitalRead(PIN_BTN_1);
  currentStateBtn2 = digitalRead(PIN_BTN_2);

  changeDiceButton();
  rollDiceButton();

}

void changeDiceButton() {
  if (currentStateBtn1 != lastReadableStateBtn1) {
    lastDebounceTimeBtn1 = millis();
    lastReadableStateBtn1 = currentStateBtn1;
  }

  if ((millis() - lastDebounceTimeBtn1) > DEBOUNCE_DELAY_BTN_1) {
    if (lastSteadyStateBtn1 == HIGH && currentStateBtn1 == LOW) {
      ++diceNumber;
      Serial.println(diceNumber); //why does this stay 1 lmao 
      }
    else if (lastSteadyStateBtn1 == LOW && currentStateBtn1 == HIGH)
      Serial.println("Button 1 is released chief");

    //save the last state
    lastSteadyStateBtn1 = currentStateBtn1;
  }
}

  void rollDiceButton() {
    if (currentStateBtn2 != lastReadableStateBtn2) {
      lastDebounceTimeBtn2 = millis();
      lastReadableStateBtn2 = currentStateBtn2;
    }

    if ((millis() - lastDebounceTimeBtn2) > DEBOUNCE_DELAY_BTN_2) {
      if (lastSteadyStateBtn2 == HIGH && currentStateBtn2 == LOW)
        Serial.println("Roll die");
      else if (lastSteadyStateBtn2 == LOW && currentStateBtn2 == HIGH)
        Serial.println("Button 2 s released chief");

      //save the last state
      lastSteadyStateBtn2 = currentStateBtn2;
    }

  }

  
