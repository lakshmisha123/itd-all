variable "inbound_rules" {
   type = list(object({
     from_port = number
     to_port = number
     protocol = string
     cidr_blocks = list(string)
   }))
}