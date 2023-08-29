************
Alert Schema
************

Effective Alerts
================

Definition
----------

Any item that is monitored must have alerts that identify the item and its issue. These alerts can be reactive or predictive.

* A reactive alert identifies a problem after it occurs. It will include
  
    * Time of initial issue
    * Status of issue (resolved or ongoing) 
  
* A predictive alert identifies that a problem will arise in the future. It will include
  
    * Percent certainty that the issue will arise
    * Time frame in which the problem may arise 

Reactive Alerts
---------------

This effort will focus on reactive alerts. An effective reactive alert will follow these steps:

#. Check that the item exists

    * If it doesn't, that's a problem in itself and should raise a separate alert 
  
#. Check if the item is within established parameters

    * Is there an exact value it should be? (Binary or categorical data)
    * Is there a threshold of allowed values? (Sampler-based data)
    * Is there a new functional addition? (e.g. A new frequency component) 
  
#. Send information to the appropriate person(s)

#. Be noticed and properly interpreted by the appropriate person(s)

    * The alert needs to make it clear that there is a problem which requires action
    * The alert should not get lost in a sea of other alerts 
  
#. Prompt an appropriate action

#. Alert all who should be aware that an issue occurred

    * Observers whose data was affected 
  
#. Document that the issue occurred

    * Record how the issue was resolved so that it's easier to fix in the future
    * Maintain data on repeated issues 

Out of Scope
------------

In the future, we may develop predictive alerts. These alerts may consider:

* The age of a hardware component compared to its lifetime
* Machine-learning-based analysis of historical errors compared to current conditions 

Items to Monitor
================

To get a handle on the type of monitoring that is needed, we must first understand the core characteristics that define "something that should be monitored." Some defining questions are:

* How is it recorded?

    * Not recorded
    * Recorded on paper
    * Recorded in FITS files
    * Recorded in a database 

* What type of data is it?

    * Qualitative

        * Categorical 

    * Quantitative

        * Static binary (one good value, all others are bad)
        * Time-series (independent variable = time)
        * Space-series (independent variable = some spatial value) 

* Is it monitored already?

    * CLEO messages
    * Ops logs
    * Grafana
    * Cron job
    * Manual inspection (e.g. audio in control room, looking for cracks in the track)
    * Individual software 

* What values or changes are indicative of a problem?

    * Data takes on a specific, bad value
    * Data goes outside of a threshold
    * Data takes on a new functional component
    * Hardware shows signs of fatigue (e.g. cracks, rust) 
