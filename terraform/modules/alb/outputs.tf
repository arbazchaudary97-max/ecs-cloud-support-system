output "alb_arn" {
  value = aws_lb.main.arn
}

output "alb_dns_name" {
  value = aws_lb.main.dns_name
}

output "target_group_arn" {
  value = aws_lb_target_group.ecs.arn
}

output "alb_zone_id" {
  value = aws_lb.main.zone_id
}