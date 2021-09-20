/* Program name: NBA dat.cpp

    Author: Chris Kiger

    Date last updated: 5/3/21

    Purpose: connect to database to retrieve and add records */

#include <iostream>
#include <string>
#include <climits>

#include "sqlite3.h"

using namespace std;

// prototypes
int mainMenu();
void printMainMenu();
void viewDivision(sqlite3 *);
void viewTeam(sqlite3 *);
void viewGame(sqlite3 *);
void addTeam(sqlite3 *);
void addPlayer(sqlite3 *);
void addGame(sqlite3 *);


int main()
{
	int choice;
    sqlite3 *mydb;
	int rc;
    
    // open database
	rc = sqlite3_open_v2("NBA.db", &mydb, SQLITE_OPEN_READWRITE, NULL);
	if(rc != SQLITE_OK)
    {
        cout << "Error in connection: " << sqlite3_errmsg(mydb);
		return 1;
    }
	
	cout << "Welcome to the NBA" << endl;
	
	// call main menu and start function based on choice
	choice = mainMenu();
	while (true)
	{
		switch (choice) 
		{
			case 1: viewDivision(mydb); break;
			case 2: viewTeam(mydb); break;
			case 3: viewGame(mydb); break;
			case 4: addTeam(mydb); break;
			case 5: addPlayer(mydb); break;
			case 6: addGame(mydb); break;
			case -1: 
			{
				sqlite3_close(mydb);
				return 0;
			}
			default: cout << "That is not a valid choice." << endl;
		}
		cout << "\n\n";
		choice = mainMenu();
	}
}

// output for menu
void printMainMenu() 
{
	cout << "Please choose an option (enter -1 to quit):  " << endl;
	cout << "1. View a Division" << endl;
	cout << "2. View a Team" << endl;
	cout << "3. View a game" << endl;
	cout << "4. Add a Team" << endl;
	cout << "5. Add a Player" << endl;
	cout << "6. Add a game" << endl;
	cout << "Enter Choice: ";
}

// input verification for menu choices
int mainMenu()
{
	int choice = 0;
	printMainMenu();
	cin >> choice;
	while ((!cin || choice < 1 || choice > 6) && choice  != -1)
	{		
		if (!cin)
		{
			cin.clear();
			cin.ignore(INT_MAX,'\n');
		}
		cout << "That is not a valid choice." << endl << endl;
		printMainMenu();
		cin >> choice;
	} 
	return choice;
}

// returns all teams in selected division
void viewDivision(sqlite3 *db)
{
    string query = "SELECT * FROM Division";
    sqlite3_stmt *result;
    int rc;
    
    rc = sqlite3_prepare_v2(db, query.c_str(), -1, &result, NULL);
    if(rc != SQLITE_OK)
    {
        cout << "Error in selection: " << endl;
        sqlite3_finalize(result);
        sqlite3_exec(db, "rollback", NULL, NULL, NULL);
	    return;
    }
    
    cout << "Please choose a division" << endl;
    int columnCount = sqlite3_column_count(result);
    int i = 1, choice;
    int divison_Name_column = 0;
    for(int j = 0; j < columnCount; j++)
    {
        string colName = sqlite3_column_name(result, j);
        if(colName == "division_Name")
        {
            divison_Name_column = j;
        }
    }
    
    rc = sqlite3_step(result);
    
    while(rc == SQLITE_ROW)
    {
        cout << i << ". " << sqlite3_column_text(result, 0) << " of the " 
        << sqlite3_column_text(result, 1) << " Conference" << endl;
        i++;
        rc = sqlite3_step(result);
    }
    
    cin >> choice;
    while(!cin || choice < 1 || choice > (i - 1))
    {
        if(!cin)
        {
            cin.clear();
            cin.ignore(INT_MAX, '\n');
        }
        cout << "That is not a valid choice! Try again!" << endl;
        cin >> choice;
    }
    
    sqlite3_reset(result);
    for(int j = 0; j < choice; j++)
    {
        sqlite3_step(result);
    }
    string division_Name = reinterpret_cast<const char*>(sqlite3_column_text(result, 0));
    sqlite3_finalize(result);
    i = 1;
    
    query = "SELECT * FROM Team WHERE division_name = '" + division_Name + "';";
    rc = sqlite3_prepare_v2(db, query.c_str(), -1, &result, NULL);
    if(rc != SQLITE_OK)
    {
        cout << "Error in selection: " << endl;
        sqlite3_finalize(result);
        sqlite3_exec(db, "rollback", NULL, NULL, NULL);
	    return;
    }
    
    columnCount = sqlite3_column_count(result);
    int team_Name_column = 0;
    for(int j = 0; j < columnCount; j++)
    {
        string colName = sqlite3_column_name(result, j);
        if(colName == "team_Name")
        {
            team_Name_column = j;
        }
    }
    
    rc = sqlite3_step(result);
    
    while(rc == SQLITE_ROW)
    {
        cout << i << ". " << sqlite3_column_text(result, 0) << endl;
        i++;
        rc = sqlite3_step(result);
    }
    
    return;
}

// shows all attributes of select team and its players
void viewTeam(sqlite3 *db)
{
    string query = "SELECT * FROM Team";
    sqlite3_stmt *result;
    int rc;
    
    rc = sqlite3_prepare_v2(db, query.c_str(), -1, &result, NULL);
    if(rc != SQLITE_OK)
    {
        cout << "Error in selection: " << endl;
        sqlite3_finalize(result);
        sqlite3_exec(db, "rollback", NULL, NULL, NULL);
	    return;
    }
    
    cout << "Please choose a team" << endl;
    int columnCount = sqlite3_column_count(result);
    int i = 1, choice;
    int team_Name_column = 0;
    for(int j = 0; j < columnCount; j++)
    {
        string colName = sqlite3_column_name(result, j);
        if(colName == "team_Name")
        {
            team_Name_column = j;
        }
    }
    
    rc = sqlite3_step(result);
    
    while(rc == SQLITE_ROW)
    {
        cout << i << ". " << sqlite3_column_text(result, 0) << endl;
        i++;
        rc = sqlite3_step(result);
    }
    
    cin >> choice;
    while(!cin || choice < 1 || choice > (i - 1))
    {
        if(!cin)
        {
            cin.clear();
            cin.ignore(INT_MAX, '\n');
        }
        cout << "That is not a valid choice! Try again!" << endl;
        cin >> choice;
    }
    
    sqlite3_reset(result);
    for(int j = 0; j < choice; j++)
    {
        sqlite3_step(result);
    }
    string team_Name = reinterpret_cast<const char*>(sqlite3_column_text(result, 0));
    string coach_Name = reinterpret_cast<const char*>(sqlite3_column_text(result, 6));
    string mascot = reinterpret_cast<const char*>(sqlite3_column_text(result, 2));
    string city = reinterpret_cast<const char*>(sqlite3_column_text(result, 3));
    string state = reinterpret_cast<const char*>(sqlite3_column_text(result, 4));
    string arena = reinterpret_cast<const char*>(sqlite3_column_text(result, 5));
    sqlite3_finalize(result);
    i = 1;
    
    query = "SELECT * FROM Player WHERE team_Name = '" + team_Name + "';";
    rc = sqlite3_prepare_v2(db, query.c_str(), -1, &result, NULL);
    if(rc != SQLITE_OK)
    {
        cout << "Error in selection: " << endl;
        sqlite3_finalize(result);
        sqlite3_exec(db, "rollback", NULL, NULL, NULL);
	    return;
    }
    
    columnCount = sqlite3_column_count(result);
    int player_Name_column = 0;
    for(int j = 0; j < columnCount; j++)
    {
        string colName = sqlite3_column_name(result, j);
        if(colName == "player_Fname")
        {
            player_Name_column = j;
        }
    }
    
    rc = sqlite3_step(result);
    
    cout << "Team: " << team_Name << endl;
    cout << "Head Coach: " << coach_Name << endl;
    cout << "Mascot: " << mascot << endl;
    cout << "Located: " << city << ", " << state << endl;
    cout << "Home Arena:" << arena << endl << endl;
    cout << "Players:" << endl;
    
    while(rc == SQLITE_ROW)
    {
        cout << i << ". " << sqlite3_column_text(result, 0) << " "
        << sqlite3_column_text(result, 1) << " # " 
        << sqlite3_column_text(result, 3) << endl;
        i++;
        rc = sqlite3_step(result);
    }
    
    
    return;
}

// retrieves all atributes of specific game
void viewGame(sqlite3 *db)
{
    string query = "SELECT * FROM Game";
    sqlite3_stmt *result;
    int rc;
    
    rc = sqlite3_prepare_v2(db, query.c_str(), -1, &result, NULL);
    if(rc != SQLITE_OK)
    {
        cout << "Error in selection: " << endl;
        sqlite3_finalize(result);
        sqlite3_exec(db, "rollback", NULL, NULL, NULL);
	    return;
    }
    
    cout << "Please choose a game" << endl;
    int columnCount = sqlite3_column_count(result);
    int i = 1, choice;
    int game_ID_column = 0;
    for(int j = 0; j < columnCount; j++)
    {
        string colName = sqlite3_column_name(result, j);
        if(colName == "game_ID")
        {
            game_ID_column = j;
        }
    }
    
    rc = sqlite3_step(result);
    
    while(rc == SQLITE_ROW)
    {
        cout << i << ". " << sqlite3_column_text(result, 1) << " vs " 
        << sqlite3_column_text(result, 2) << " on " 
        << sqlite3_column_text(result, 6) << endl;
        i++;
        rc = sqlite3_step(result);
    }
    
    cin >> choice;
    while(!cin || choice < 1 || choice > (i - 1))
    {
        if(!cin)
        {
            cin.clear();
            cin.ignore(INT_MAX, '\n');
        }
        cout << "That is not a valid choice! Try again!" << endl;
        cin >> choice;
    }
    
    sqlite3_reset(result);
    for(int j = 0; j < choice; j++)
    {
        sqlite3_step(result);
    }
    //sqlite3_finalize(result);
    
    cout << "Date: " << sqlite3_column_text(result, 6) << endl;
    cout << "Home Team: " << sqlite3_column_text(result, 1) << endl;
    cout << "Away Team: " << sqlite3_column_text(result, 2) << endl;
    cout << "Arena: " << sqlite3_column_text(result, 5) << endl;
    cout << "Winner: " << sqlite3_column_text(result, 3) << endl;
    cout << "Score: " << sqlite3_column_text(result, 4) << endl;
  
    return;
}

// adds a new team to database
void addTeam(sqlite3 *db)
{
    string query = "SELECT * FROM Division";
    sqlite3_stmt *result;
    int rc;
    
    rc = sqlite3_prepare_v2(db, query.c_str(), -1, &result, NULL);
    if(rc != SQLITE_OK)
    {
        cout << "Error in selection: " << endl;
        sqlite3_finalize(result);
        sqlite3_exec(db, "rollback", NULL, NULL, NULL);
	    return;
    }
    
    cout << "Please choose a division to add a team to" << endl;
    int columnCount = sqlite3_column_count(result);
    int i = 1, choice;
    int divison_Name_column = 0;
    for(int j = 0; j < columnCount; j++)
    {
        string colName = sqlite3_column_name(result, j);
        if(colName == "division_Name")
        {
            divison_Name_column = j;
        }
    }
    
    rc = sqlite3_step(result);
    
    while(rc == SQLITE_ROW)
    {
        cout << i << ". " << sqlite3_column_text(result, 0) << " of the " 
        << sqlite3_column_text(result, 1) << " Conference" << endl;
        i++;
        rc = sqlite3_step(result);
    }
    
    cin >> choice;
    while(!cin || choice < 1 || choice > (i - 1))
    {
        if(!cin)
        {
            cin.clear();
            cin.ignore(INT_MAX, '\n');
        }
        cout << "That is not a valid choice! Try again!" << endl;
        cin >> choice;
    }
    
    sqlite3_reset(result);
    for(int j = 0; j < choice; j++)
    {
        sqlite3_step(result);
    }
    string division_Name = reinterpret_cast<const char*>(sqlite3_column_text(result, 0));
    sqlite3_finalize(result);
    
    string team_Name, mascot, city, state, arena, head_Coach; 
    
    cin.ignore(INT_MAX, '\n');
    cout << "Enter the team's name:" << endl;
    getline(cin, team_Name);
    cout << "Enter the team's mascot:" << endl;
    getline(cin, mascot);
    cout << "Enter the team's city:" << endl;
    getline(cin, city);
    cout << "Enter the team's state:" << endl;
    getline(cin, state);
    cout << "Enter the team's arena:" << endl;
    getline(cin, arena);
    cout << "Enter the team's head coach:" << endl;
    getline(cin, head_Coach);
    
    query = "INSERT INTO team (team_Name, division_Name, mascot, city, state, arena, head_Coach) VALUES ('" + team_Name + "', '" + division_Name + "', '" + mascot + "', '" + city + "', '" + state + "', '" + arena + "', '" + head_Coach + "');";
    //cout << query << endl;
    
    
    rc = sqlite3_exec(db, query.c_str(), NULL, NULL, NULL);
     if(rc != SQLITE_OK)
    {
        cout << "Error in insertion: " << endl;
        sqlite3_finalize(result);
        sqlite3_exec(db, "rollback", NULL, NULL, NULL);
	    return;
    }
    
    sqlite3_exec(db, "commit", NULL, NULL, NULL);
    cout << "Successfully inserted Team" << endl;
    return;
}

// adds a new player to database
void addPlayer(sqlite3 *db)
{
    string query = "SELECT * FROM Team";
    sqlite3_stmt *result;
    int rc;
    
    rc = sqlite3_prepare_v2(db, query.c_str(), -1, &result, NULL);
    if(rc != SQLITE_OK)
    {
        cout << "Error in selection: " << endl;
        sqlite3_finalize(result);
        sqlite3_exec(db, "rollback", NULL, NULL, NULL);
	    return;
    }
    
    cout << "Please choose a team to add a player to" << endl;
    int columnCount = sqlite3_column_count(result);
    int i = 1, choice;
    int team_Name_column = 0;
    for(int j = 0; j < columnCount; j++)
    {
        string colName = sqlite3_column_name(result, j);
        if(colName == "team_Name")
        {
            team_Name_column = j;
        }
    }
    
    rc = sqlite3_step(result);
    
    while(rc == SQLITE_ROW)
    {
        cout << i << ". " << sqlite3_column_text(result, 0) << endl;
        i++;
        rc = sqlite3_step(result);
    }
    
    cin >> choice;
    while(!cin || choice < 1 || choice > (i - 1))
    {
        if(!cin)
        {
            cin.clear();
            cin.ignore(INT_MAX, '\n');
        }
        cout << "That is not a valid choice! Try again!" << endl;
        cin >> choice;
    }
    
    sqlite3_reset(result);
    for(int j = 0; j < choice; j++)
    {
        sqlite3_step(result);
    }
    string team_Name = reinterpret_cast<const char*>(sqlite3_column_text(result, 0));
    sqlite3_finalize(result);
    
    string player_Fname, player_Lname, number; 
    
    cin.ignore(INT_MAX, '\n');
    cout << "Enter the player's first name:" << endl;
    getline(cin, player_Fname);
    cout << "Enter the player's last name:" << endl;
    getline(cin, player_Lname);
    cout << "Enter the player's number:" << endl;
    getline(cin, number);
    
    query = "INSERT INTO player (player_Fname, player_Lname, team_Name, number) VALUES ('" + player_Fname+ "', '" + player_Lname + "', '" + team_Name + "', '" + number + "');";
    //cout << query << endl;
    
    
    rc = sqlite3_exec(db, query.c_str(), NULL, NULL, NULL);
     if(rc != SQLITE_OK)
    {
        cout << "Error in insertion: " << endl;
        sqlite3_finalize(result);
        sqlite3_exec(db, "rollback", NULL, NULL, NULL);
	    return;
    }
    
    sqlite3_exec(db, "commit", NULL, NULL, NULL);
    cout << "Successfully inserted player" << endl;
    return;
}

// adds a new game to database
void addGame(sqlite3 *db)
{
    string query = "SELECT * FROM Team";
    sqlite3_stmt *result;
    int rc;
    
    rc = sqlite3_prepare_v2(db, query.c_str(), -1, &result, NULL);
    if(rc != SQLITE_OK)
    {
        cout << "Error in selection: " << endl;
        sqlite3_finalize(result);
        sqlite3_exec(db, "rollback", NULL, NULL, NULL);
	    return;
    }
    
    cout << "Please choose the home team" << endl;
    int columnCount = sqlite3_column_count(result);
    int i = 1, choice;
    int team_Name_column = 0;
    for(int j = 0; j < columnCount; j++)
    {
        string colName = sqlite3_column_name(result, j);
        if(colName == "team_Name")
        {
            team_Name_column = j;
        }
    }
    
    rc = sqlite3_step(result);
    
    while(rc == SQLITE_ROW)
    {
        cout << i << ". " << sqlite3_column_text(result, 0) << endl;
        i++;
        rc = sqlite3_step(result);
    }
    
    cin >> choice;
    while(!cin || choice < 1 || choice > (i - 1))
    {
        if(!cin)
        {
            cin.clear();
            cin.ignore(INT_MAX, '\n');
        }
        cout << "That is not a valid choice! Try again!" << endl;
        cin >> choice;
    }
    
    sqlite3_reset(result);
    for(int j = 0; j < choice; j++)
    {
        sqlite3_step(result);
    }
    string home = reinterpret_cast<const char*>(sqlite3_column_text(result, 0));
    string arena = reinterpret_cast<const char*>(sqlite3_column_text(result, 5));
    
    sqlite3_reset(result);
    cout << "Please choose the away team" << endl;
    columnCount = sqlite3_column_count(result);
    i = 1;
    int choice2;
    team_Name_column = 0;
    for(int j = 0; j < columnCount; j++)
    {
        string colName = sqlite3_column_name(result, j);
        if(colName == "team_Name")
        {
            team_Name_column = j;
        }
    }
    
    rc = sqlite3_step(result);
    
    while(rc == SQLITE_ROW)
    {
        cout << i << ". " << sqlite3_column_text(result, 0) << endl;
        i++;
        rc = sqlite3_step(result);
    }
    
    cin >> choice2;
    while(!cin || choice2 < 1 || choice2 > (i - 1) || choice2 == choice)
    {
        if(!cin)
        {
            cin.clear();
            cin.ignore(INT_MAX, '\n');
        }
        cout << "That is not a valid choice! Try again!" << endl;
        cin >> choice;
    }
    
    sqlite3_reset(result);
    for(int j = 0; j < choice2; j++)
    {
        sqlite3_step(result);
    }
    string away = reinterpret_cast<const char*>(sqlite3_column_text(result, 0));
    sqlite3_finalize(result);
    
    string winner, score, date; 
    
    cin.ignore(INT_MAX, '\n');
    cout << "Enter the winner of the game:" << endl;
    getline(cin, winner);
    cout << "Enter the score of the game:" << endl;
    getline(cin, score);
    cout << "Enter the date of the game:" << endl;
    getline(cin, date);
    
    query = "INSERT INTO game (home, away, winner, score, arena, date) VALUES ('" + home + "', '" + away + "', '" + winner + "', '" + score + "', '" + arena + "', '" + date + "');";
    cout << query << endl;
    
    
    rc = sqlite3_exec(db, query.c_str(), NULL, NULL, NULL);
     if(rc != SQLITE_OK)
    {
        cout << "Error in insertion: " << endl;
        sqlite3_finalize(result);
        sqlite3_exec(db, "rollback", NULL, NULL, NULL);
	    return;
    }
    
    sqlite3_exec(db, "commit", NULL, NULL, NULL);
    cout << "Successfully inserted game" << endl;
    return;
}
    //int rc = sqlite3_exec(db, "Begin Transaction", NULL, NULL, &err);
    //error(rc, 1);