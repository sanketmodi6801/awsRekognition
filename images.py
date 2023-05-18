import boto3

s3 = boto3.resource('s3')

# Get list of objects for indexing
images=[('me.jpeg','sanket'),
      ('me1.jpg','modi'),
      ('elon.jpg','elon musk'),
      ('mark.jpg','mark zukerberg'),
      ('bill.jpg','bill gates')
      ]

# Iterate through list to upload objects to S3   
for image in images:
    file = open(image[0],'rb')
    object = s3.Object('bucketeg','index/'+ image[0])
    ret = object.put(Body=file,
                    Metadata={'FullName':image[1]})