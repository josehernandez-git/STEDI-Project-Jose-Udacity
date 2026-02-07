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

# Script generated for node Step Trainer Landing
StepTrainerLanding_node1769971656955 = glueContext.create_dynamic_frame.from_options(format_options={"multiLine": "false"}, connection_type="s3", format="json", connection_options={"paths": ["s3://jose-501/step_trainer/landing"], "recurse": True}, transformation_ctx="StepTrainerLanding_node1769971656955")

# Script generated for node Customer Curated
CustomerCurated_node1769971707084 = glueContext.create_dynamic_frame.from_options(format_options={"multiLine": "false"}, connection_type="s3", format="json", connection_options={"paths": ["s3://jose-501/customer/curated/"], "recurse": True}, transformation_ctx="CustomerCurated_node1769971707084")

# Script generated for node SQL Query
SqlQuery2102 = '''
select step_trainer_landing.*
from step_trainer_landing
  join customer_curated on customer_curated.serialnumber = step_trainer_landing.serialnumber;
'''
SQLQuery_node1769971722687 = sparkSqlQuery(glueContext, query = SqlQuery2102, mapping = {"customer_curated":CustomerCurated_node1769971707084, "step_trainer_landing":StepTrainerLanding_node1769971656955}, transformation_ctx = "SQLQuery_node1769971722687")

# Script generated for node Step Trainer Trusted
StepTrainerTrusted_node1769971785577 = glueContext.getSink(path="s3://jose-501/step_trainer/trusted/", connection_type="s3", updateBehavior="UPDATE_IN_DATABASE", partitionKeys=[], enableUpdateCatalog=True, transformation_ctx="StepTrainerTrusted_node1769971785577")
StepTrainerTrusted_node1769971785577.setCatalogInfo(catalogDatabase="project",catalogTableName="step_trainer_trusted")
StepTrainerTrusted_node1769971785577.setFormat("json")
StepTrainerTrusted_node1769971785577.writeFrame(SQLQuery_node1769971722687)
job.commit()
