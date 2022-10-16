import monsterjobs_scraper

job_type = input('Job Type: ')
job_location = input('City to search in: ')

#!python3
# scraper.py - pulls data from monster and indeed.

monsterjobs_scraper.main(job_type, job_location)