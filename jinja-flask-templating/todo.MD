1. Set up a route to /guess/some_name.
2. Parse the URL to extract the name at the end of the URL.
3. Make sure the name is in Title case.
4. Make two API calls to genderize.io and agify.io in order to obtain the "gender and the "age"
    for the name at the end of the URL.
5. Insert the result from the API call into the template.


#Format

'Hey [name],'

'I think you are [gender],'

'And maybe [age] years old.'