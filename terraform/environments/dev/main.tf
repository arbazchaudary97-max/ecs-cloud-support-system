module "vpc" {
  source = "../../modules/vpc"
}

module "security_groups" {
  source = "../../modules/security-groups"

  vpc_id = module.vpc.vpc_id
}

module "alb" {
  source = "../../modules/alb"

  vpc_id                = module.vpc.vpc_id
  public_subnet_ids     = module.vpc.public_subnet_ids
  alb_security_group_id = module.security_groups.alb_security_group_id
  certificate_arn       = module.acm.certificate_arn
}

module "ecs" {
  source = "../../modules/ecs"

  private_subnet_ids    = module.vpc.private_subnet_ids
  ecs_security_group_id = module.security_groups.ecs_security_group_id
  target_group_arn      = module.alb.target_group_arn
  ecr_image_uri         = "520900723145.dkr.ecr.eu-west-2.amazonaws.com/ecs-cloud-support-system:latest"

  depends_on = [module.alb]
}

module "acm" {
  source = "../../modules/acm"

  domain_name = "ecscloudsupport.com"
  zone_id     = "Z0834957I96OH8NRVSQ2"
}
