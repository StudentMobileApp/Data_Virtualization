#include <windows.h>

// Current version of OpenGL, which I'm not using atm
// If you want to check these out, I can send you the files. 
// Note: You will also have to change some settings in VS
// #include <GL/glew.h> 
// #include <GLFW/glfw3.h>

#include <gl/Gl.h>
#include <gl/Glu.h>
#include <stdlib.h>
#include "glut.h"
#include <time.h> //for Sierpinski demonstration

// Inner class for storing a 2D integer point. 
// There are different ways of doing this
class GLintPoint
{
	public:
		GLint x;
		GLint y;

		GLintPoint() {};
		GLintPoint(int a, int b)
		{
			x = a;
			y = b;
		}
};

// Declares functions
void Display();
void Init(void);
void Cartesion(void);
void Sierpinski(void);
void drawDot(GLint x, GLint y);
int random(int num);

#define height 600
#define width 600

//remember, we're dealing with pixels
#define centerX 300
#define centerY 300
#define numUnits 200

void main(int argc, char** argv)
{
	// Initializes the GLUT library(toolkits)
	glutInit(&argc, argv);

	// Sets the diaplay mode. Additional buffering choice here.
	glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB);

	// Sets the window size
	glutInitWindowSize(height, width);

	// Sets up the sreen window using a top-left coordinate.
	glutInitWindowPosition(300, 100);

	// Creates the title of the window
	glutCreateWindow("Sierpinski and soon, Cartesion");

	// Creates Cartesion by calling its function
	// Registers the display callback function glutDisplayFunc(Display);
	//glutDisplayFunc(Sierpinski);
	glutDisplayFunc(Cartesion);

	// Implements other necessary initializations
	Init();

	// A function in GLUT is used to give a non-stop loop to run the application until the next event runs.
	glutMainLoop();
}

// For Sierpinski. 
// Makes a function to return random integer number in the range
int random(int num)
{
	return rand() % num;
}


// Draws Cartesion lines. Called function has to have (void).
void Cartesion(void)
{
	// Clears the color buffer
	glClear(GL_COLOR_BUFFER_BIT);

	//drawing the x-axis from left to right
	glBegin(GL_LINES); 
	glVertex2i(centerX - numUnits, centerY); // i for int (there is d and f, too)
	glVertex2i(centerX + numUnits, centerY);
	glEnd();

	//drawing the y-axis from left to right
	glBegin(GL_LINES); //drawing lines
	glVertex2i(centerX, centerY - numUnits);
	glVertex2i(centerX, centerY + numUnits);
	glEnd();

	glFlush();
}

// For demonstraion purposes
void Sierpinski(void)
{
	srand(time(0));

	// Builds a GLintPoint array and assigns values to the points
	GLintPoint p[3] = { {10, 10}, {620, 30}, {360, 460} };

	// Randomly selects a index from 0 to 2
	int idx = random(3);

	// Builds a new GLintPoint storing the selected the point
	GLintPoint point = p[idx];

	// Clears the color buffer
	glClear(GL_COLOR_BUFFER_BIT);

	// Draws the selected point by using drawDot function 
	drawDot(point.x, point.y);

	// Builds a loop for drawing the Pierpinski
	for (int i = 0; i < 12000; i++)
	{
		idx = random(3);
		point.x = (point.x + p[idx].x) / 2;
		point.y = (point.y + p[idx].y) / 2;
		drawDot(point.x, point.y);
	}
	glFlush();
}

// Makes a function using to draw a dot.
void drawDot(GLint x, GLint y)
{
	glBegin(GL_POINTS);
	glVertex2i(x, y);
	glEnd();
}

// Displays three points on the screen.
void Display()
{
	// Clear the color buffer
	glClear(GL_COLOR_BUFFER_BIT);

	// Begins to draw the points
	/*
	predrawing of main object can be put here if established points are needed
	*/

	glBegin(GL_POINTS);
	glVertex2i(100, 50);
	glVertex2i(100, 200);
	glVertex2i(250, 130);

	// Ends the drawing
	glEnd();

	// Sends the output result to the screen. Don't forget this!
	glFlush();
}

// Sets up a function for initializing other necessary attributes
void Init()
{
	// Sets up the background color to white
	glClearColor(1.0, 1.0, 1.0, 0.0);

	// Sets up the color of the graph
	glColor3f(0.0f, 0.0f, 0.0f); //can interpret int as double

	// Sets up the size of the point in size by size pixel
	glPointSize(2.6);

	glMatrixMode(GL_PROJECTION);
	glLoadIdentity();

	// This function is used to clipping the window in 2D
	gluOrtho2D(0.0, height, 0.0, width);
}