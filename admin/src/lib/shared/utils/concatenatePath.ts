export const concatenatePath = (...args: string[]) => {
    return '/' + args.map(a => a.split('/')).flat().filter(p => p !== '').join('/')
}
