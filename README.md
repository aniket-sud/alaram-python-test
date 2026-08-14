# CLI Alarm Clock

## Overview

This project implements a command-line alarm clock in Python.

The original requirement was intentionally open-ended, so assumptions and design decisions were made to deliver a complete, maintainable solution within a short timeframe.

---


### Provided Requirement

Build an Alarm Clock as a Python CLI application.

### Assumptions

The application should:

- Run entirely in terminal.
- Allow a user to create alarms.
- Allow a user to view alarms.
- Allow deletion of alarms.
- Trigger alarms automatically.
- Support multiple alarms.

### Non Goals

To keep the solution focused:

- No GUI
- No database
- No persistence after restart
- No external services

---

## Features

### Add Alarm

Create a new alarm.

### List Alarms

Display all scheduled alarms.

### Remove Alarm

Delete an alarm before it triggers.

### Alarm Trigger

Automatically triggers when scheduled time arrives.

---

## Design Decisions

### In-Memory Storage

Chosen for simplicity and speed of implementation.

### Background Thread

The CLI remains responsive while alarms are monitored in parallel.

### Validation

The program validates:

- Date/time format
- Future timestamps only

---

## Architecture

Main Thread
- User interaction
- Command processing

Background Thread
- Alarm monitoring
- Trigger execution

---

## AI Usage

AI was used for:

- Requirement refinement
- Architecture planning
- Identifying edge cases
- Generating implementation ideas

All generated output was manually reviewed, tested, and validated before final submission.

---

## Running

Install Python 3.10+

Run:

python alarm_clock.py

---

## Example

add

2026-08-14 18:30:00

Interview Reminder

list

exit

---

## Future Improvements

- Persistent storage
- Snooze functionality
- Sound notification
- Recurring alarms
- Automated tests