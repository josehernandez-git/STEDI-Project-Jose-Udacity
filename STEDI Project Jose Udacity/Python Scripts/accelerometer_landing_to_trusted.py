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

# Script generated for node Accelerometer landing
Accelerometerlanding_node1769968501305 = glueContext.create_dynamic_frame.from_options(format_options={"multiLine": "false"}, connection_type="s3", format="json", connection_options={"paths": ["s3://jose-501/accelerometer/landing/"], "recurse": True}, transformation_ctx="Accelerometerlanding_node1769968501305")

# Script generated for node Customer Trusted
CustomerTrusted_node1769968575533 = glueContext.create_dynamic_frame.from_options(format_options={"multiLine": "false"}, connection_type="s3", format="json", connection_options={"paths": ["s3://jose-501/customer/trusted/"], "recurse": True}, transformation_ctx="CustomerTrusted_node1769968575533")

# Script generated for node Filter opt-in customers
SqlQuery2077 = '''
select accelerometer_landing.*
from accelerometer_landing
  join customer_trusted on customer_trusted.email = accelerometer_landing.user;
'''
Filteroptincustomers_node1769968781874 = sparkSqlQuery(glueContext, query = SqlQuery2077, mapping = {"accelerometer_landing":Accelerometerlanding_node1769968501305, "customer_trusted":CustomerTrusted_node1769968575533}, transformation_ctx = "Filteroptincustomers_node1769968781874")

# Script generated for node Accelerometer trusted
Accelerometertrusted_node1769968885333 = glueContext.getSink(path="s3://jose-501/accelerometer/trusted/", connection_type="s3", updateBehavior="UPDATE_IN_DATABASE", partitionKeys=[], enableUpdateCatalog=True, transformation_ctx="Accelerometertrusted_node1769968885333")
Accelerometertrusted_node1769968885333.setCatalogInfo(catalogDatabase="project",catalogTableName="accelerometer_trusted")
Accelerometertrusted_node1769968885333.setFormat("json")
Accelerometertrusted_node1769968885333.writeFrame(Filteroptincustomers_node1769968781874)
job.commit()
