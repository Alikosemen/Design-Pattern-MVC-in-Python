# MVC Applications in Python

## Overview

This repository is dedicated to showcasing Model-View-Controller (MVC) applications developed in Python. The MVC architecture is a widely used architectural pattern in software engineering, especially useful for designing applications with a clear separation of concerns.

## About MVC

Model–View–Controller (MVC) is a software architecture, currently considered an architectural pattern used in software engineering. The pattern is structured into three main components:

- **Model**: The Model represents the application's dynamic data structure, independent of the user interface. It directly manages the data, logic, and rules of the application.

- **View**: The View displays data to the user based on the information received from the Model. It represents the visualization of the data that model contains.

- **Controller**: The Controller acts as an interface between Model and View components to process all the business logic and incoming requests, manipulate data using the Model, and interact with the Views to render the final output.

![MVC Diagram](https://upload.wikimedia.org/wikipedia/commons/thumb/a/a0/MVC-Process.svg/1200px-MVC-Process.svg.png)

*Diagram illustrating the MVC pattern. (Image source: Wikimedia Commons)*

## Projects in This Repository

Each folder in this repository contains a separate application implementing the MVC pattern in Python. Here are some of the projects you can find:

### Test Management System

This project implements a Test Management System (TMS) with the following functionalities:

 ![Test Management System SQLite DB](/TMS_DB_Photo.png)

- **Query a Specific Defect**: When a user queries for a particular defect, the system displays the summary of the defect in a prescribed format. This allows for quick and detailed viewing of defect specifics directly through the interface.

- **Search by Component**: The system provides a functionality where the user can search by component name to display a list of all defects logged against that component. This is useful for analyzing the frequency and severity of issues associated with particular parts of a project.

 

These features are implemented to enhance the efficiency and usability of managing defects within software development and testing processes.


Feel free to explore the projects and enhance them with your contributions.

## Getting Started

To get started with these projects, clone the repository and navigate to each project folder:

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name/project-folder
