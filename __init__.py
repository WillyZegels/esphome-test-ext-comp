import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import climate, uart
from esphome.const import (
    CONF_ID
    CONF_UART_ID
    CONF_RECEIVE_TIMEOUT
    
from esphome.const import (
    CONF_ID, 
    CONF_TRIGGER_ID
)

DEPENDENCIES = {'uart'}
CVsolarDrivec_ns = cg.esphome_ns.namespace('CVsolarDrive')
CVsolarDriveC = CVsolarDrivec_ns.class_('CVsolarDriveC', uart.UARTDevice, cg.Component)

CONFIG_SCHEMA = cv.COMPONENT_SCHEMA.extend(
{
    cv.GenerateID(): cv.declare_id(CVsolarDriveC),
    cv.required(CONF_LAMBDA): cv.returning_lambda,
    cv.required(CONF_CLIMATES): cv.ensure_list(climate.CLIMATE_SCHEMA),
})
    .extend(cv.polling_component_schema("10s"))

async def to_code(config):
    uart_component = await cg.get_variable(config[CONF_UART_ID])
    var = cg.new_Pvariable(config[CONF_ID])
    await cg.register_component(var, config
    