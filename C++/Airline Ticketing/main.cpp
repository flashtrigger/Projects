/*
Program name: Airline Ticketing System
Author: Chris Kiger
Date last updated: 13APRIL2021
Purpose: The program allows the user to look at seating chart and pick a seat
*/

#include <bits/stdc++.h>
 
using namespace std;


class Passenger{

  private:
    string fName;
    string lName;
    int connectingFlightNumber;
    time_t queueTime;
  
  public:
    Passenger();

  Passenger(string first, string last, int flightNum, time_t t): fName(first), lName(last), connectingFlightNumber(flightNum), queueTime(t){};

  string getfName(){
    return fName;
  }

  string getlName(){
    return lName;
  }

  int getConnectingFlightNumber(){
    return connectingFlightNumber;
  }

  int getQueueTime(){
    return queueTime;
  }
};

void enqueue();
string front();
string deque();
int getSize();
bool isEmpty();

const int ROWS = 13;
const int COLUMNS = 6;

void initiailzeSeatPlan(char sPlan[][COLUMNS], int rowSize);
void showSeatAssignments(char sPlan[][COLUMNS], int rowSize);
void assignSeat(char sPlan[][COLUMNS], int rowSize);
void showMenu(char sPlan[][COLUMNS], int rowSize);

bool isFirstClassFull(char sPlan[][COLUMNS], int rowSize);
bool isBusinessClassFull(char sPlan[][COLUMNS], int rowSize);
bool isEconomyClassFull(char sPlan[][COLUMNS], int rowSize);

void selectSeatNumber(int startRows, int endRows, int& rowNo, char& columnNo);

void assignFirstClassSeat(char sPlan[][COLUMNS], int rowSize);

void assignSeatBusinessClass(char sPlan[][COLUMNS], int rowSize);
void assignSeatEconomyClass(char sPlan[][COLUMNS], int rowSize);

int main(){

	char seatPlan[ROWS][COLUMNS];
	char resp;

  ifstream readFile;
  ofstream writeFile;

	initiailzeSeatPlan(seatPlan, ROWS);

  readFile.open("seat.txt");

  for(int i = 0; i < COLUMNS; i++){
    for(int j = 0; j < ROWS; j++){
      readFile.get(seatPlan[i][j]);
    }
  }

  readFile.close();

	showMenu(seatPlan, ROWS);

	cout << "Would you like to reserve a set? Please enter Y/y(Yes), N/n(No): " << endl;
	cin >> resp;
	cout << endl;
	
	while (resp == 'y' || resp == 'Y'){

		assignSeat(seatPlan, ROWS);

    writeFile.open("seat.txt");
    for(int i = 0; i < COLUMNS; i++){
      for(int j = 0; j < ROWS; j++){
        writeFile << seatPlan[i][j];
      }
    }

    writeFile.close();


		showMenu(seatPlan, ROWS);
		cout << "Would you like to reserve another seat? Y/y(Yes), N/n(No): ";
		cin >> resp;
		cout << endl;
	}

	return 0;
}

void initiailzeSeatPlan(char sPlan[][COLUMNS], int rowSize){

	int i, j;

	for (i = 0; i < rowSize; i++)
		for (j = 0; j < COLUMNS; j++)
			sPlan[i][j] = '*';
}

void showSeatAssignments(char sPlan[][COLUMNS], int rowSize){

	int i, j;

	cout << "        A B C  D E F" << endl;

	for (i = 0; i < rowSize; i++){

		cout << "Row " << setw(2) << i+1 << "  ";
		for (j = 0; j < COLUMNS; j++){

			cout << sPlan[i][j] << " ";
			if (j == 2)
				cout << " ";
		}
		cout << endl;
	}

	cout << "* -- available seat" << endl;
	cout << "X -- occupied seat" << endl;
	cout << endl;
}

void assignSeat(char sPlan[][COLUMNS], int rowSize){

	char ticketClass;
	char resp;
  string fname, lname;
  int flightNum;
  queue<Passenger> firstClassQueue;
  queue<Passenger> businessClassQueue;
  queue<Passenger> economyClassQueue;
 
	cout << "Please enter the ticket class: F/f (First Class); "
		<< " (B/b) (Business Class); E/e (Economy Class): ";
	cin >> ticketClass;
	cout << endl;
			
	switch (ticketClass){
  
	case 'f': 
	case 'F':	
    if (!isFirstClassFull(sPlan, rowSize))
        assignFirstClassSeat(sPlan, rowSize);
    else{
        cout << "We are sorry, but First Class is Full. Would you like to loin the waiting list? Y/y(Yes), N/n(No):";
        cin >> resp;
        cout << endl;
    }

    break;

  case 'b': 
	case 'B':	
    if (!isBusinessClassFull(sPlan, rowSize))
        assignSeatBusinessClass(sPlan, rowSize);
    else{
        cout << "We are sorry, but Business Class is Full. Would you like to loin the waiting list? Y/y(Yes), N/n(No):";
        cout << "Press Y/y to continue: ";
        cin >> resp;
        cout << endl;
    }

    break;

	case 'e': 
	case 'E':	
    if (!isEconomyClassFull(sPlan, rowSize))
        assignSeatEconomyClass(sPlan, rowSize);
    else{
      cout << "We are sorry, but Economy Class is Full. Would you like to loin the waiting list? Y/y(Yes), N/n(No):";
      cout << "Press Y/y to continue: ";
      cin >> resp;
      cout << endl;
    }
  }

    showSeatAssignments(sPlan, rowSize);
}

void showMenu(char sPlan[][COLUMNS], int rowSize){

  cout << "This program allows you to reserve a seat on an airplane." << endl;
  cout << "The current seat assignments are: " << endl;
  showSeatAssignments(sPlan, rowSize);
  cout << "Rows 1 and 2 are for First Class passengers." << endl;
  cout << "Rows 3 through 7 are for Business Class passengers." << endl;
  cout << "Rows 8 through 13 are for Economy Class passengers." << endl;
}

bool isFirstClassFull(char sPlan[][COLUMNS], int rowSize){

  int i, j;
  int assignedSeats = 0;

  for (i = 0; i < 2; i++)
    for (j = 0; j < COLUMNS; j++)
      if (sPlan[i][j] == 'X')
        assignedSeats++;

  return (assignedSeats == 2 * COLUMNS);
}

bool isBusinessClassFull(char sPlan[][COLUMNS], int rowSize){

  int i, j;
  int assignedSeats = 0;

  for (i = 2; i < 7; i++)
    for (j = 0; j < COLUMNS; j++)
      if (sPlan[i][j] == 'X')
        assignedSeats++;

  return (assignedSeats == 5 * COLUMNS);
}

bool isEconomyClassFull(char sPlan[][COLUMNS], int rowSize){

  int i, j;
  int assignedSeats = 0;

  for (i = 7; i < 13; i++)
    for (j = 0; j < COLUMNS; j++)
      if (sPlan[i][j] == 'X')
        assignedSeats++;

  return (assignedSeats == 6 * COLUMNS);
}

void selectSeatNumber(int startRows, int endRows, int& rowNo, char& columnNo){

  cout << "Enter Row number " << startRows << " - " << endRows << ": ";
  cin >> rowNo;
  cout << endl;

  while (rowNo < startRows || rowNo > endRows){

    cout << "Enter Row number " << startRows << " - " << endRows << ": ";
    cin >> rowNo;
    cout << endl;
  }

  cout << "Enter seat letter (A - F): ";
  cin >> columnNo;
  cout << endl;

  while (columnNo < 'A' || columnNo > 'F'){

    cout << "Enter seat letter (A - F): ";
    cin >> columnNo;
    cout << endl;
  }
}

void assignFirstClassSeat(char sPlan[][COLUMNS], int rowSize){

  int rowNum;
  char columnPos;

  if (!isFirstClassFull(sPlan, rowSize)){

    selectSeatNumber(1, 2, rowNum, columnPos);

    while (sPlan[rowNum - 1][columnPos -65] != '*'){

      cout << "*#*#*#*# This seat is occupied *#*#*#*#" << endl;
      cout << "Make another selection" << endl;

      showSeatAssignments(sPlan, rowSize);
  
      selectSeatNumber(1, 2, rowNum, columnPos);
    }

    sPlan[rowNum - 1][columnPos - 65] = 'X';
    cout << "This seat is reserved for you" << endl;
  }
  else
    cout << "Sorry!!! First Class is Full" << endl;
}

void assignSeatBusinessClass(char sPlan[][COLUMNS], int rowSize){

  int rowNum;
  char columnPos;

  if (!isBusinessClassFull(sPlan, rowSize)){

    selectSeatNumber(3, 7, rowNum, columnPos);

    while (sPlan[rowNum - 1][columnPos -65] != '*'){

      cout << "*#*#*#*# This seat is occupied *#*#*#*#" << endl;
      cout << "Make another selection" << endl;

      showSeatAssignments(sPlan, rowSize);
  
      selectSeatNumber(3, 7, rowNum, columnPos);
    }

    sPlan[rowNum - 1][columnPos - 65] = 'X';
    cout << "This seat is reserved for you" << endl;
  }
  else
    cout << "Business class is full." << endl;
}

void assignSeatEconomyClass(char sPlan[][COLUMNS], int rowSize){

  int rowNum;
  char columnPos;

  if (!isEconomyClassFull(sPlan, rowSize)){

    selectSeatNumber(8, 13, rowNum, columnPos);

    while (sPlan[rowNum - 1][columnPos -65] != '*'){
      
      cout << "*#*#*#*# This seat is occupied *#*#*#*#" << endl;
      cout << "Make another selection" << endl;

      showSeatAssignments(sPlan, rowSize);
  
      selectSeatNumber(8, 13, rowNum, columnPos);
    }

    sPlan[rowNum - 1][columnPos -65] = 'X';
    cout << "This seat is reserved for you" << endl;
  }
  else
    cout << "Economic class is full." << endl;
}