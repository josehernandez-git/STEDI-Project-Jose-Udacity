import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue import DynamicFrame

def sparkSqlQuery(glueContext, query, mapping, transformation_ctx) -> DynamicFrame:
    for alias, frame in mapping.items():
        frame.toDF().createOrReplaceTempView(alias)
    result = spark.sql(query)
    return DynamicFrame.fromDF(result, glueContext, transformation_ctx)
args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Script generated for node Accelerometer Landing Zone
AccelerometerLandingZone_node1769970544798 = glueContext.create_dynamic_frame.from_options(format_options={"multiLine": "false"}, connection_type="s3", format="json", connection_options={"paths": ["s3://jose-501/accelerometer/landing/"], "recurse": True}, transformation_ctx="AccelerometerLandingZone_node1769970544798")

# Script generated for node Customers Trusted Zone
CustomersTrustedZone_node1769970481422 = glueContext.create_dynamic_frame.from_options(format_options={"multiLine": "false"}, connection_type="s3", format="json", connection_options={"paths": ["s3://jose-501/customer/trusted/"], "recurse": True}, transformation_ctx="CustomersTrustedZone_node1769970481422")

# Script generated for node SQL Query
SqlQuery2451 = '''
select distinct customer_trusted.*
from customer_trusted
  join accelerometer_landing on accelerometer_landing.user = customer_trusted.email;
'''
SQLQuery_node1769970608891 = sparkSqlQuery(glueContext, query = SqlQuery2451, mapping = {"accelerometer_landing":AccelerometerLandingZone_node1769970544798, "customer_trusted":CustomersTrustedZone_node1769970481422}, transformation_ctx = "SQLQuery_node1769970608891")

# Script generated for node Customer Curated
CustomerCurated_node1769971246041 = glueContext.getSink(path="s3://jose-501/customer/curated/", connection_type="s3", updateBehavior="UPDATE_IN_DATABASE", partitionKeys=[], enableUpdateCatalog=True, transformation_ctx="CustomerCurated_node1769971246041")
CustomerCurated_node1769971246041.setCatalogInfo(catalogDatabase="project",catalogTableName="customer_curated")
CustomerCurated_node1769971246041.setFormat("json")
CustomerCurated_node1769971246041.writeFrame(SQLQuery_node1769970608891)
job.commit()
